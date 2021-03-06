"""empty message

Revision ID: 04000f03332b
Revises: 
Create Date: 2021-02-13 16:36:35.656011

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04000f03332b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todoapp',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todoapp')
    # ### end Alembic commands ###
