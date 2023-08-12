-- SafeDive takes in two parameters and
-- returns their quotient
DELIMITER $$;

CREATE FUNCTION SafeDiv (a INT, b INT) RETURN FLOAT
BEGIN
	IF b == 0 THEN
		RETURN 0;
	END IF;
	RETURN (a/b);
END $$;

DELIMITER ;
