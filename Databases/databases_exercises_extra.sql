CREATE TABLE `products_per_invoice`(
    `invoice_number (PK, FK)` BIGINT NOT NULL,
    `product_code (PK, FK)` BIGINT NOT NULL,
    `quantity` INT NOT NULL,
    `total_amount` DECIMAL(8, 2) NOT NULL
);
CREATE TABLE `invoices`(
    `number (PK)` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `buyer_id (FK)` BIGINT NOT NULL,
    `method_id (FK)` BIGINT NOT NULL,
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
    `buyer_id (PK, FK)` LINESTRING NOT NULL,
    PRIMARY KEY(`buyer_id (PK, FK)`)
);
CREATE TABLE `shopping_cart_product`(
    `buyer_id (PK, FK)` LINESTRING NOT NULL,
    `product_code (PK, FK)` BIGINT NOT NULL,
    `quantity` INT NOT NULL,
    `total_amount` DECIMAL(8, 2) NOT NULL
);
CREATE TABLE `users`(
    `id (PK)` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `full_name` LINESTRING NOT NULL,
    `email` LINESTRING NOT NULL,
    `registration_date` DATE NOT NULL
);
ALTER TABLE
    `users` ADD UNIQUE `users_email_unique`(`email`);
CREATE TABLE `reviews`(
    `review_id (PK)` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `owner_id (FK)` BIGINT NOT NULL,
    `product_code (FK)` BIGINT NOT NULL,
    `comment` LINESTRING NOT NULL,
    `rating` TINYINT NOT NULL,
    `review_date` DATE NOT NULL
);
ALTER TABLE
    `reviews` ADD UNIQUE `reviews_owner_id (fk)_unique`(`owner_id (FK)`);
ALTER TABLE
    `reviews` ADD UNIQUE `reviews_product_code (fk)_unique`(`product_code (FK)`);
CREATE TABLE `payment_methods`(
    `pay_id (PK)` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `method_type` LINESTRING NOT NULL,
    `bank_name` LINESTRING NULL
);
ALTER TABLE
    `shopping_cart_product` ADD CONSTRAINT `shopping_cart_product_product_code (pk, fk)_foreign` FOREIGN KEY(`product_code (PK, FK)`) REFERENCES `products`(`code (PK)`);
ALTER TABLE
    `invoices` ADD CONSTRAINT `invoices_method_id (fk)_foreign` FOREIGN KEY(`method_id (FK)`) REFERENCES `payment_methods`(`pay_id (PK)`);
ALTER TABLE
    `products_per_invoice` ADD CONSTRAINT `products_per_invoice_product_code (pk, fk)_foreign` FOREIGN KEY(`product_code (PK, FK)`) REFERENCES `products`(`code (PK)`);
ALTER TABLE
    `reviews` ADD CONSTRAINT `reviews_owner_id (fk)_foreign` FOREIGN KEY(`owner_id (FK)`) REFERENCES `users`(`id (PK)`);
ALTER TABLE
    `shopping_cart` ADD CONSTRAINT `shopping_cart_buyer_id (pk, fk)_foreign` FOREIGN KEY(`buyer_id (PK, FK)`) REFERENCES `users`(`id (PK)`);
ALTER TABLE
    `shopping_cart_product` ADD CONSTRAINT `shopping_cart_product_buyer_id (pk, fk)_foreign` FOREIGN KEY(`buyer_id (PK, FK)`) REFERENCES `shopping_cart`(`buyer_id (PK, FK)`);
ALTER TABLE
    `products_per_invoice` ADD CONSTRAINT `products_per_invoice_invoice_number (pk, fk)_foreign` FOREIGN KEY(`invoice_number (PK, FK)`) REFERENCES `invoices`(`number (PK)`);
ALTER TABLE
    `invoices` ADD CONSTRAINT `invoices_buyer_id (fk)_foreign` FOREIGN KEY(`buyer_id (FK)`) REFERENCES `users`(`id (PK)`);
ALTER TABLE
    `reviews` ADD CONSTRAINT `reviews_product_code (fk)_foreign` FOREIGN KEY(`product_code (FK)`) REFERENCES `products`(`code (PK)`);