"""initial

Revision ID: b64a4712d1ce
Revises: 
Create Date: 2024-05-22 17:48:28.774437

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b64a4712d1ce'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('unit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('unit_name', sa.String(length=100), nullable=True),
    sa.Column('short_name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('short_name'),
    sa.UniqueConstraint('unit_name')
    )
    op.create_table('enum_classifier',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('unit_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['enum_classifier.id'], ),
    sa.ForeignKeyConstraint(['unit_id'], ['unit.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('prod_class',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('class_name', sa.String(length=100), nullable=True),
    sa.Column('unit_id', sa.Integer(), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['prod_class.id'], ),
    sa.ForeignKeyConstraint(['unit_id'], ['unit.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('class_name')
    )
    op.create_table('enum_position',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('short_name', sa.String(), nullable=True),
    sa.Column('integer_value', sa.Integer(), nullable=True),
    sa.Column('real_value', sa.Float(), nullable=True),
    sa.Column('string_value', sa.String(), nullable=True),
    sa.Column('classifier_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['classifier_id'], ['enum_classifier.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('param',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('short_name', sa.String(length=20), nullable=True),
    sa.Column('unit_id', sa.Integer(), nullable=True),
    sa.Column('enum_classifier_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['enum_classifier_id'], ['enum_classifier.id'], ),
    sa.ForeignKeyConstraint(['unit_id'], ['unit.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('product',
    sa.Column('id_product', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(length=150), nullable=True),
    sa.Column('prod_class_id', sa.Integer(), nullable=True),
    sa.Column('enum_classifier_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['enum_classifier_id'], ['enum_classifier.id'], ),
    sa.ForeignKeyConstraint(['prod_class_id'], ['prod_class.id'], ),
    sa.PrimaryKeyConstraint('id_product'),
    sa.UniqueConstraint('product_name')
    )
    op.create_table('param_class',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('min_value', sa.Integer(), nullable=True),
    sa.Column('max_value', sa.Integer(), nullable=True),
    sa.Column('param_id', sa.Integer(), nullable=True),
    sa.Column('prodclass_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['param_id'], ['param.id'], ),
    sa.ForeignKeyConstraint(['prodclass_id'], ['prod_class.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('param_product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('param_class_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['param_class_id'], ['param_class.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id_product'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('param_product')
    op.drop_table('param_class')
    op.drop_table('product')
    op.drop_table('param')
    op.drop_table('enum_position')
    op.drop_table('prod_class')
    op.drop_table('enum_classifier')
    op.drop_table('unit')
    # ### end Alembic commands ###