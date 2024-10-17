-- Script to create an index on the first letter of the name column in the names table.

-- Drop the existing index if it exists.
CREATE INDEX idx_name_first
 ON names(name(1));

