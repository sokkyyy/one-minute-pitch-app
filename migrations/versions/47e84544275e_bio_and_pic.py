"""bio and pic

Revision ID: 47e84544275e
Revises: 603f344d024d
Create Date: 2019-10-20 17:19:38.699042

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47e84544275e'
down_revision = '603f344d024d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(), nullable=True))
    op.add_column('users', sa.Column('pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pic_path')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###