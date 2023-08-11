-- Selects a list of bands from the metal_bands table
-- that play the `Glam rock` style and computes how long
-- they've been existing.
SELECT band_name, COALESCE(split, 2022) - formed AS lifespan
	FROM metal_bands
	WHERE FIND_IN_SET('Glam rock', style)
	ORDER BY lifespan DESC; 
