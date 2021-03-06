"""Add the analysis_requests table.

Revision ID: a0433904c63b
Revises: 22a1cd66a9c6
Create Date: 2016-05-16 08:55:08.751761

"""

# revision identifiers, used by Alembic.
revision = 'a0433904c63b'
down_revision = '22a1cd66a9c6'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    """Upgrade the database to a newer revision."""
    # commands auto generated by Alembic - please adjust! ###
    op.create_table('analysis_requests',
                    sa.Column('ecosystem', sa.Integer(), nullable=True),
                    sa.Column('package', sa.String(length=255), nullable=True),
                    sa.Column('version', sa.String(length=255), nullable=True),
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('job_id', sa.String(length=255), nullable=True),
                    sa.Column('submitted_at', sa.DateTime(), nullable=True),
                    sa.Column('fulfilled_at', sa.DateTime(), nullable=True),
                    sa.Column('analysis_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['analysis_id'], ['analyses.id'], ),
                    sa.PrimaryKeyConstraint('id'))
    op.create_index('epv_index', 'analysis_requests', ['ecosystem', 'package', 'version'],
                    unique=True, postgresql_where=sa.text('fulfilled_at IS NULL'))
    # end Alembic commands ###


def downgrade():
    """Downgrade the database to an older revision."""
    # commands auto generated by Alembic - please adjust! ###
    op.drop_table('analysis_requests')
    # end Alembic commands ###
