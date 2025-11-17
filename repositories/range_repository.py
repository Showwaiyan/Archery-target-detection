from database import execute_query


async def get_total_arrows_per_end(range_id: int):
    sql = f"SELECT rangeTotalArrowsPerEnd FROM `range` WHERE rangeID = %s"
    rows = await execute_query(sql, (range_id,))
    if len(rows) == 0:
        return None

    result = rows[0]["rangeTotalArrowsPerEnd"]
    return result
