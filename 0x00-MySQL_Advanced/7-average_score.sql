-- Creates procedure that computes average score
-- for students projects
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$;
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	UPDATE users
	SET average_score=(SELECT AVG(score) FROM corrections
			   WHERE corrections.user_id = users_id)
	WHERE id=user_id;
END;$$
DELIMITER ;
