-- Procedure to compute and store the average score for a specified user.
-- Input: user_id - the ID of the user whose average score is to be computed.

DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser$$

CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    DECLARE avg_score FLOAT;

    -- Calculate the average score for the user from the corrections table
    SELECT AVG(score) INTO avg_score 
    FROM corrections 
    WHERE user_id = user_id;

    -- Update the average score for the user in the users table
    UPDATE users 
    SET average_score = IFNULL(avg_score, 0) -- If no scores, set average_score to 0
    WHERE id = user_id;

END $$

DELIMITER ;

