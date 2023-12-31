-- Rank country of bands by number of fans
-- from the metal_band table.
SELECT origin, SUM(fans) as nb_fans 
	FROM metal_bands
	GROUP BY origin
	ORDER BY nb_fans DESC;  
