"""empty message

Revision ID: 68e7503e0da5
Revises: None
Create Date: 2016-03-04 02:59:22.899049

"""

# revision identifiers, used by Alembic.
revision = '68e7503e0da5'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('graphs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('graph_json', postgresql.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('graphs')
    ### end Alembic commands ###