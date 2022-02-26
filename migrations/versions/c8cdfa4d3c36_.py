"""empty message

Revision ID: c8cdfa4d3c36
Revises: 
Create Date: 2022-02-24 20:39:29.549778

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8cdfa4d3c36'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('video_id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=10000), nullable=False),
    sa.Column('created_at_date', sa.String(length=100), nullable=False),
    sa.Column('created_at_time', sa.TIME(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('subscriber_count', sa.Integer(), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('videos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=5000), nullable=False),
    sa.Column('video_url', sa.String(length=1000), nullable=False),
    sa.Column('views', sa.Integer(), nullable=False),
    sa.Column('created_at_date', sa.String(length=100), nullable=False),
    sa.Column('created_at_time', sa.TIME(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('videos')
    op.drop_table('users')
    op.drop_table('comments')
    # ### end Alembic commands ###
