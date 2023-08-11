-- Create a trigger after an insert on the `order`
-- table and updates the `items` table
CREATE TRIGGER red AFTER INSERT ON order
	FOR EACH ROW UPDATE items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
