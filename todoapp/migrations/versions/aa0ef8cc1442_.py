"""empty message

Revision ID: aa0ef8cc1442
Revises: f1aad7f2e55f
Create Date: 2021-02-15 17:38:20.871354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa0ef8cc1442'
down_revision = 'f1aad7f2e55f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todolists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('todoapp', sa.Column('list_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'todoapp', 'todolists', ['list_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todoapp', type_='foreignkey')
    op.drop_column('todoapp', 'list_id')
    op.drop_table('todolists')
    # ### end Alembic commands ###