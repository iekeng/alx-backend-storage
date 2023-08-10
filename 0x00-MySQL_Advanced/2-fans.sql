-- Rank country of bands by number of fans
-- from the metal_band table.
SELECT country, SUM(fans) as nb_fans 
	GROUP BY origin 
	ORDER BY nb_fans;
