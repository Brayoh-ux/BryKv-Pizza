"""pizza table

Revision ID: 47cf8144c2bb
Revises: 
Create Date: 2021-03-05 05:29:06.627455

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47cf8144c2bb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('pizza',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pizza', sa.String(), nullable=True),
    sa.Column('pizza_amount', sa.Integer(), nullable=True),
    sa.Column('p_size', sa.String(), nullable=True),
    sa.Column('crust', sa.String(), nullable=True),
    sa.Column('crust_amount', sa.String(), nullable=True),
    sa.Column('toppings', sa.String(), nullable=True),
    sa.Column('top_size', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pizza_crust'), 'pizza', ['crust'], unique=True)
    op.create_index(op.f('ix_pizza_crust_amount'), 'pizza', ['crust_amount'], unique=True)
    op.create_index(op.f('ix_pizza_p_size'), 'pizza', ['p_size'], unique=True)
    op.create_index(op.f('ix_pizza_pizza'), 'pizza', ['pizza'], unique=True)
    op.create_index(op.f('ix_pizza_pizza_amount'), 'pizza', ['pizza_amount'], unique=True)
    op.create_index(op.f('ix_pizza_top_size'), 'pizza', ['top_size'], unique=True)
    op.create_index(op.f('ix_pizza_toppings'), 'pizza', ['toppings'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_pizza_toppings'), table_name='pizza')
    op.drop_index(op.f('ix_pizza_top_size'), table_name='pizza')
    op.drop_index(op.f('ix_pizza_pizza_amount'), table_name='pizza')
    op.drop_index(op.f('ix_pizza_pizza'), table_name='pizza')
    op.drop_index(op.f('ix_pizza_p_size'), table_name='pizza')
    op.drop_index(op.f('ix_pizza_crust_amount'), table_name='pizza')
    op.drop_index(op.f('ix_pizza_crust'), table_name='pizza')
    op.drop_table('pizza')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
