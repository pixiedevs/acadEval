from django.contrib.auth.models import User
from django.db.models import fields
from import_export import resources
from import_export.widgets import ForeignKeyWidget, Widget
from .models import Contact
from student.models import Student, StudentAttendance


class ContactResource(resources.ModelResource):
    class Meta:
        model = Contact
        exclude = ('id', )


class StudentAttendanceResource(resources.ModelResource):
    # user_id = fields.Field(db_column='user', Widget=ForeignKeyWidget(User, 'username'))

    class Meta:
        model = StudentAttendance
        skip_unchanged = True
        report_skipped = True
        exclude = ('id', )
        fields = ('student__student_id', 'semester', 'date', 'is_present')
        import_id_fields = ('student__student_id',)


# Below code is in development
class StudentResource(resources.ModelResource):
    # user_id = fields.Field(db_column='user', Widget=ForeignKeyWidget(User, 'username'))
    
    class Meta:
        model = Student
        skip_unchanged = True
        report_skipped = True
        exclude = ('id', )
        fields = ('user__username', 'first_name', 'last_name', 'email', 'father_name', 'student_id', 'enrollment', 'mobile_no', 'gender', 'father_mobile_no',
                            'current_address', 'permanent_address', 'branch', 'batch_year', 'semester', 'year', 'date_of_birth', 'guardian_name', 'guardian_mobile_no')
        import_id_fields = ('username', 'first_name', 'last_name', 'email', 'father_name', 'student_id', 'enrollment', 'mobile_no', 'gender', 'father_mobile_no',
                            'current_address', 'permanent_address', 'branch', 'batch_year', 'semester', 'year', 'date_of_birth', 'guardian_name', 'guardian_mobile_no')

    def before_import_row(self, row, **kwargs):
        username = row.get('username')
        print(username)
        password = row.get('password')

        (user, created) = User.objects.get_or_create(username=username, password=password)
        row['user'] = user.id

    def get_instance(self, instance_loader, row):
        try:
            params = {}
            for key in instance_loader.resource.get_import_id_fields():
                field = instance_loader.resource.fields[key]
                params[field.attribute] = field.clean(row)
            return self.get_queryset().get(**params)
        except Exception:
            return None
