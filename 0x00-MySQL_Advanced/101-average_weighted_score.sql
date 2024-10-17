-- DELIMITER $$ allows for the use of ; within the procedure without prematurely ending it.

DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users
    SET average_score = (
        SELECT IFNULL(SUM(c.score * p.weight) / NULLIF(SUM(p.weight), 0), 0)
        FROM corrections c
        INNER JOIN projects p ON p.id = c.project_id
        WHERE c.user_id = users.id
    );
END $$

DELIMITER ;

