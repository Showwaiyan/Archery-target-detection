from database import execute_query


async def insert_an_arrow_to_staging(
    roundID, participationID, distance, endOrder, arrowScore, isX
):
    sql = """
        INSERT INTO arrowStaging
        (roundID, participationID, distance, endOrder, arrowScore, isX, stagingStatus, date)
        VALUES (%s, %s, %s, %s, %s, %s, 'pending', NOW())
        """
    await execute_query(
        sql,
        (
            roundID,
            participationID,
            distance,
            endOrder,
            arrowScore,
            isX,
        ),
    )

    return True
