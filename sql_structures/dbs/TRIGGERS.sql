DELIMITER //

-- cuando se hace una venta, reducir existencias
DROP TRIGGER IF EXISTS reducir_existencias_inventario//

CREATE TRIGGER reducir_existencias_inventario BEFORE INSERT ON Venta FOR EACH ROW
BEGIN
	UPDATE Cafe SET Libras = Libras - (SELECT cantidad FROM Venta_has_Cafe WHERE Venta_idVenta = NEW.id)
    WHERE id = (SELECT Cafe_idCafe FROM Venta_has_Cafe WHERE Venta_idVenta = NEW.id);

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