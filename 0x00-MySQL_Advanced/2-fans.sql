-- This script ranks country origins of bands,
-- ordered by the number of (non-unique) fans

DROP FUNCTION IF EXISTS fans;

DELIMITER //
CREATE FUNCTION fans(orig VARCHAR(255))
RETURNS INTEGER DETERMINISTIC
BEGIN
    DECLARE total_fans INTEGER;
    SELECT SUM(fans) INTO total_fans FROM metal_bands WHERE origin = orig;
    RETURN total_fans;
END //
DELIMITER ;

SELECT origin, fans(origin) AS nb_fans FROM metal_bands GROUP BY origin ORDER BY nb_fans DESC;