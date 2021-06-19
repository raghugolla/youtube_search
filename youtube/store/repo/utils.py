import re

from shuttlis.pagination import Cursor
from sqlalchemy import and_, or_, desc
from sqlalchemy.orm.attributes import InstrumentedAttribute


def process_search_string(search_phrase: str) -> str:
    # match partial words in tsquery
    search_phrase = re.sub("[^A-Za-z0-9]+", " ", search_phrase)
    return " & ".join([f"{word}:*" for word in search_phrase.split()])


def paginated_results(
    query,
    model,
    cursor: Cursor,
    order=None,
    timestamp_attr: InstrumentedAttribute = None,
):
    """
    Given a SQLAlchemy Query object, executes it with the given pagination
    parameters.

    Every model that is passed in here is expected to contain two fields:

    - id

    Results are ordered by (created_at, id) by default.
    """

    if order == "desc":
        if timestamp_attr is None:
            timestamp_attr = model.created_at
        t = type(timestamp_attr)
        if cursor.after:
            query = query.filter(
                or_(
                    timestamp_attr < cursor.after_date,
                    and_(
                        timestamp_attr == cursor.after_date, model.id < cursor.after_id,
                    ),
                )
            )  # yapf: disable

        return (
            query.order_by(desc(timestamp_attr), desc(model.id))
            .limit(cursor.limit)
            .all()
        )
    else:
        if timestamp_attr is None:
            timestamp_attr = model.created_at
        t = type(timestamp_attr)
        if cursor.after:
            query = query.filter(
                or_(
                    timestamp_attr > cursor.after_date,
                    and_(
                        timestamp_attr == cursor.after_date, model.id > cursor.after_id,
                    ),
                )
            )  # yapf: disable

        return query.order_by(timestamp_attr, model.id).limit(cursor.limit).all()
