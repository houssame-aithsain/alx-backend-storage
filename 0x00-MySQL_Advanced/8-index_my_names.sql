-- Script to create an index on the first letter of the name column in the names table.

-- Drop the existing index if it exists.
DROP INDEX IF EXISTS idx_name_first ON names;

-- Create a new index on the first letter of the name column.
CREATE INDEX idx_name_first ON names (SUBSTRING(name, 1, 1));

-- Optional: Show the indexes of the names table to confirm the new index has been created.
SHOW INDEX FROM names;

