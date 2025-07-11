CREATE TABLE ventas_resumen (
    id_venta INTEGER,
    fecha DATE,
    cliente_id INTEGER,
    producto TEXT,
    categoria TEXT,
    monto NUMERIC(10,2),
    metodo_pago TEXT,
    ciudad TEXT,
    vendedor TEXT,
    descuento_aplicado NUMERIC(5,2),
    reembolsado BOOLEAN,
    monto_total NUMERIC(10,2)
);