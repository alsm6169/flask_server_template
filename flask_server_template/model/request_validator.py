from marshmallow import ValidationError, Schema, fields, validate

'''To validate the input parameters'''
def some_custom_check(data):
    '''can be replaced with customized check'''
    if not data:
        raise ValidationError('some_custom_check for title failed')
class TitleValidator(Schema):
    '''https://marshmallow.readthedocs.io/en/stable/marshmallow.validate.html'''
    # URL should have title of type string between length 1 and 50. After that call your custom check
    title = fields.Str(required=True, validate=[validate.Length(min=1, max=50), some_custom_check])


