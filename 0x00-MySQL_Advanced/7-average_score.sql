-- This script contains a stored procedure that
-- computes and stores the average score for a student.

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser (user_id INTEGER)
BEGIN
    DECLARE average FLOAT;

    SELECT AVG(score) INTO average
    FROM corrections 
    WHERE corrections.user_id = user_id;

    UPDATE users
    SET average_score = average
    WHERE id = user_id;
END //
DELIMITER ;