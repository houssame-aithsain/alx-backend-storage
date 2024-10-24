-- Task 3: List all bands with Glam rock as their main style, ranked by longevity

SELECT band_name, (IFNULL(split, 2022) - formed)
AS lifespan FROM metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;

