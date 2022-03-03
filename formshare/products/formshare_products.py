from formshare.products import create_product, add_metadata_to_product


def register_products():
    products = []
    # A new product
    new_product = create_product("fs1import", False, "fas fa-file-import")
    add_metadata_to_product(new_product, "author", "QLands Technology Consultants")
    add_metadata_to_product(new_product, "version", "1.0")
    add_metadata_to_product(new_product, "Licence", "AGPL")
    products.append(new_product)

    new_product = create_product("xmlimport", False, "fas fa-file-import")
    add_metadata_to_product(new_product, "author", "QLands Technology Consultants")
    add_metadata_to_product(new_product, "version", "1.0")
    add_metadata_to_product(new_product, "Licence", "AGPL")
    products.append(new_product)

    new_product = create_product("repository", False, "fas fa-database")
    add_metadata_to_product(new_product, "author", "QLands Technology Consultants")
    add_metadata_to_product(new_product, "version", "1.0")
    add_metadata_to_product(new_product, "Licence", "AGPL")
    products.append(new_product)

    new_product = create_product("xlsx_public_export", False, "far fa-file-excel")
    add_metadata_to_product(new_product, "author", "QLands Technology Consultants")
    add_metadata_to_product(new_product, "version", "1.0")
    add_metadata_to_product(new_product, "Licence", "AGPL")
    products.append(new_product)

    new_product = create_product("xlsx_private_export", False, "far fa-file-excel")
    add_metadata_to_product(new_product, "author", "QLands Technology Consultants")
    add_metadata_to_product(new_product, "version", "1.0")
    add_metadata_to_product(new_product, "Licence", "AGPL")
    products.append(new_product)

    new_product = create_product("media_export", False, "far fa-images")
    add_metadata_to_product(new_product, "author", "QLands Technology Consultants")
    add_metadata_to_product(new_product, "version", "1.0")
    add_metadata_to_product(new_product, "Licence", "AGPL")
    products.append(new_product)

    new_product = create_product("kml_export", False, "fas fa-map-marker-alt")
    add_metadata_to_product(new_product, "author", "QLands Technology Consultants")
    add_metadata_to_product(new_product, "version", "1.0")
    add_metadata_to_product(new_product, "Licence", "AGPL")
    products.append(new_product)

    new_product = create_product("csv_public_export", False, "fas fa-file-csv")
    add_metadata_to_product(new_product, "author", "QLands Technology Consultants")
    add_metadata_to_product(new_product, "version", "1.0")
    add_metadata_to_product(new_product, "Licence", "AGPL")
    products.append(new_product)

    new_product = create_product("csv_private_export", False, "fas fa-file-csv")
    add_metadata_to_product(new_product, "author", "QLands Technology Consultants")
    add_metadata_to_product(new_product, "version", "1.0")
    add_metadata_to_product(new_product, "Licence", "AGPL")
    products.append(new_product)

    new_product = create_product("merge_form", False, "fas fa-sync-alt")
    add_metadata_to_product(new_product, "author", "QLands Technology Consultants")
    add_metadata_to_product(new_product, "version", "1.0")
    add_metadata_to_product(new_product, "Licence", "AGPL")
    products.append(new_product)

    new_product = create_product("zip_csv_public_export", False, "far fa-file-archive")
    add_metadata_to_product(new_product, "author", "QLands Technology Consultants")
    add_metadata_to_product(new_product, "version", "1.0")
    add_metadata_to_product(new_product, "Licence", "AGPL")
    products.append(new_product)

    new_product = create_product("zip_csv_private_export", False, "far fa-file-archive")
    add_metadata_to_product(new_product, "author", "QLands Technology Consultants")
    add_metadata_to_product(new_product, "version", "1.0")
    add_metadata_to_product(new_product, "Licence", "AGPL")
    products.append(new_product)

    return products
