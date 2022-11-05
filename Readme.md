#sellis
#Exam
# Issue and Solve it

Issue List :
1. RuntimeError: Model class movies.models.Movie doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.
solve: Movie app were not added in settings INSTALLED_APPS

2. django.db.utils.IntegrityError: The row in table 'movies_movie' with primary key '1' has an invalid foreign key: movies_movie.creator_id contains a value 'wewe' that does not have a corresponding value in auth_user.id.
Solve: There was a explict valu in movies_movie record where creator id was wewe . I change it to a correct value

3. No connection between auth register 
solve: added url in main Urls api/v1/auth

4. AssertionError: May not set both `read_only` and `required`
solve: In RegisterSerializer read_only and required can not be in same time and password cannot be a read only field. Insted of readonly used write_only and required

5. /api/v1/movies was open for anyone but for create any new movies need auth user there getting error.

solve: After step 3 now I can determine which user is authinticated or not . So , in this route added permission IsAuthenticated , so only Authenticated user can see the views

6. Every time I try to register new user It is not validating password.( "Password fields didn't match.")
solve: In serializer validate password if password and password2 same though it will raise error . I removed it.

7. Any Authenticated user can see all record
solved: Added queryset for user can only their record 

8. Details operation(Retrive/Update/Delete) can be done by anyone .
solved: Only authintacated user can retrive own record and manipulate only own records.


N.B: Admin user has all access . Admin user can access to al operation over all records.

