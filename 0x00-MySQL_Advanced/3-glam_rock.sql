-- This script lists all bands with `Glam rock`
-- as their main style, ranked by their longevity

DROP FUNCTION IF EXISTS lifespan;
DELIMITER //

CREATE FUNCTION lifespan(formed INTEGER, split INTEGER)
    RETURNS INTEGER DETERMINISTIC 
BEGIN
    IF split IS NULL THEN
        RETURN 2022 - formed;
    ELSE
        RETURN split - formed;
    END IF;
END//

DELIMITER ;

SELECT band_name, lifespan(split, formed) AS lifespan
FROM metal_bands
WHERE metal_bands.style = 'Glam rock'
ORDER BY lifespan;