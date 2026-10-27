CREATE TABLE `products_per_invoice`(
    `invoice_number (PK, FK)` BIGINT NOT NULL,
    `product_code (PK, FK)` BIGINT NOT NULL,
    `quantity` INT NOT NULL,
    `total_amount` DECIMAL(8, 2) NOT NULL
);
CREATE TABLE `invoices`(
    `number (PK)` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `buyer_email` LINESTRING NOT NULL,
    `total_amount` DECIMAL(8, 2) NOT NULL,
    `purchase_date` TIMESTAMP NOT NULL
);
CREATE TABLE `products`(
    `code (PK)` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` LINESTRING NOT NULL,
    `price` DECIMAL(8, 2) NOT NULL,
    `entry_date` TIMESTAMP NOT NULL,
    `brand` LINESTRING NOT NULL,
    `stock_availability` INT NOT NULL
);
CREATE TABLE `shopping_cart`(
    `buyer_email (PK)` LINESTRING NOT NULL,
    PRIMARY KEY(`buyer_email (PK)`)
);
CREATE TABLE `shopping_cart_product`(
    `buyer_email (PK, FK)` LINESTRING NOT NULL,
    `product_code (PK, FK)` BIGINT NOT NULL,
    `quantity` INT NOT NULL,
    `total_amount` DECIMAL(8, 2) NOT NULL
);
ALTER TABLE
    `shopping_cart_product` ADD CONSTRAINT `shopping_cart_product_product_code (pk, fk)_foreign` FOREIGN KEY(`product_code (PK, FK)`) REFERENCES `products`(`code (PK)`);
ALTER TABLE
    `products_per_invoice` ADD CONSTRAINT `products_per_invoice_product_code (pk, fk)_foreign` FOREIGN KEY(`product_code (PK, FK)`) REFERENCES `products`(`code (PK)`);
ALTER TABLE
    `shopping_cart_product` ADD CONSTRAINT `shopping_cart_product_buyer_email (pk, fk)_foreign` FOREIGN KEY(`buyer_email (PK, FK)`) REFERENCES `shopping_cart`(`buyer_email (PK)`);
ALTER TABLE
    `products_per_invoice` ADD CONSTRAINT `products_per_invoice_invoice_number (pk, fk)_foreign` FOREIGN KEY(`invoice_number (PK, FK)`) REFERENCES `invoices`(`number (PK)`);