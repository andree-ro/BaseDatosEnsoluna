DELIMITER //

-- cuando se hace una venta, reducir existencias
DROP TRIGGER IF EXISTS reducir_existencias_inventario//

CREATE TRIGGER reducir_existencias_inventario BEFORE INSERT ON Venta_has_Cafe FOR EACH ROW
BEGIN
	UPDATE Cafe SET Libras = Libras - NEW.cantidad WHERE id = NEW.Cafe_idCafe;

	UPDATE Empacado SET Cantidad = Cantidad - NEW.cantidad WHERE id = NEW.Empacado_idEmpacado;

END//

DELIMITER ;