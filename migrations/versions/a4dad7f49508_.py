"""empty message

Revision ID: a4dad7f49508
Revises: 62fe64155ef9
Create Date: 2023-07-07 18:42:13.011766

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4dad7f49508'
down_revision = '62fe64155ef9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('jobs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('project_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('jobs_user_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'projects', ['project_id'], ['id'])
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('jobs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('jobs_user_id_fkey', 'projects', ['user_id'], ['id'])
        batch_op.drop_column('project_id')

    # ### end Alembic commands ###