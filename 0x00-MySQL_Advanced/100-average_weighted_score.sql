-- Create a stored procedure to compute the average weighted score for a user
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE weighted_sum FLOAT DEFAULT 0;
    DECLARE total_weight INT DEFAULT 0;

    -- Calculate the weighted sum and total weight
    SELECT SUM(c.score * p.weight) INTO weighted_sum,
           SUM(p.weight) INTO total_weight
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    -- Calculate the average score, handling the case where total_weight is 0
    IF total_weight > 0 THEN
        UPDATE users
        SET average_score = weighted_sum / total_weight
        WHERE id = user_id;
    ELSE
        UPDATE users
        SET average_score = 0
        WHERE id = user_id;
    END IF;
END //

DELIMITER ;

