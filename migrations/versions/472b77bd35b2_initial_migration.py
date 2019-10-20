"""Initial Migration

Revision ID: 472b77bd35b2
Revises: 
Create Date: 2019-10-20 13:09:37.603784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '472b77bd35b2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pitches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pitch_category', sa.String(), nullable=True),
    sa.Column('pitch_details', sa.String(), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pitches')
    op.drop_table('users')
    # ### end Alembic commands ###