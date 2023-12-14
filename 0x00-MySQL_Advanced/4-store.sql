-- This script contains a trigger that
-- decreases the quantity of an item after
-- adding a new order

DELIMITER //
CREATE TRIGGER update_quantity AFTER INSERT ON orders
FOR EACH ROW
BEGIN
UPDATE items
SET quantity = quantity - NEW.number
WHERE items.name = NEW.item_name;
END //

DELIMITER ;