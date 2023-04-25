DELIMITER //

-- cuando se hace una venta, reducir existencias
DROP TRIGGER IF EXISTS reducir_existencias_inventario//

CREATE TRIGGER reducir_existencias_inventario BEFORE INSERT ON Venta_has_Cafe FOR EACH ROW
BEGIN
	UPDATE Cafe SET Libras = Libras - NEW.cantidad
    WHERE id = NEW.Cafe_idCafe;

END//

/* (work in progress)
-- cuando se hace una compra aumentar existencias (ya convertidas)
DROP TRIGGER IF EXISTS incrementar_existencias_inventario//

CREATE TRIGGER incrementar_existencias_inventario AFTER INSERT ON Cafe_ingreso FOR EACH ROW
BEGIN
	INSERT INTO conversion VALUES 

END//
*/

DELIMITER ;