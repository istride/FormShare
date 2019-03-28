from ..processes.db import add_product_instance, cancel_task, task_exists, get_form_used_products
from formshare.config.celery_app import celeryApp
import formshare.plugins as p
import logging
import os

__all__ = [
    'add_product', 'register_product_instance', 'product_found', 'get_products', 'stop_task', 'get_product',
    'create_product', 'add_metadata_to_product', 'get_product_directory']

log = logging.getLogger(__name__)

_PRODUCTS = []


def product_found(name):
    for product in _PRODUCTS:
        if product["code"] == name:
            return True
    return False


def get_product(name):
    for product in _PRODUCTS:
        if product["code"] == name:
            return product
    return None


def add_product(product, from_plugin=False):
    if not product_found(product["code"]):
        product['plugin'] = from_plugin
        _PRODUCTS.append(product)
    else:
        raise Exception("Product code {} is already in use".format(product["code"]))


def register_product_instance(request, user, project, form, product, task, output_file, file_mime, process_only=False):
    if product_found(product):
        add_product_instance(request, user, project, form, product, task, output_file, file_mime, process_only)


def get_products():
    return list(_PRODUCTS)


def stop_task(request, user, project, form, task):
    if task_exists(request, project, form, task):
        log.warning("Stopping task {}".format(task))
        celeryApp.control.revoke(task, terminate=True)
        log.warning("Cancelling task {} in database ".format(task))
        return cancel_task(request, user, task)
    return False, ""


def get_product_description(request, product):
    if product == "fs1import":
        return request.translate('Import data')
    if product == "repository":
        return request.translate('Build repository')
    return request.translate("Without description")


def get_form_products(request, project, form):
    result = []
    used_products = get_form_used_products(request, project, form)
    for a_product in used_products:
        a_product['desc'] = request.translate('Without description')

    for a_product in used_products:
        product_info = get_product(a_product['code'])
        if product_info is not None:
            if not product_info['plugin']:
                a_product['desc'] = get_product_description(request, a_product['code'])
                result.append(a_product)

    # Call connected plugins to get the description of their products
    for plugin in p.PluginImplementations(p.IProduct):
        for a_product in used_products:
            product_info = get_product(a_product['code'])
            if product_info is not None:
                if product_info['plugin']:
                    plugin_description = plugin.get_product_description(request, a_product['code'])
                    if plugin_description is not None:
                        a_product['desc'] = plugin_description
                    result.append(a_product)


def get_product_directory(request, project, form, product):
    try:
        if product_found(product):
            path = os.path.join(request.registry.settings['repository.path'], *['products', project, form, product])
            if not os.path.exists(path):
                os.makedirs(path)
            return path
        else:
            return None
    except Exception as e:
        log.error("Unable to create product directory for product {} in project {} form {}. Error: {}".
                  format(product, project, form, str(e)))
        return None


def create_product(product_code):
    return {"code": product_code, "metadata": {}}


def add_metadata_to_product(product, key, value):
    try:
        product["metadata"][key] = value
        return True, product
    except Exception as e:
        log.error(
            "Unable to add metadata to product {}. Key: {}. Value {}. Error: {}".format(product, key, value, str(e)))
        return False, product
