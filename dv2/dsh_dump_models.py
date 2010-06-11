#
# these are the "definition" files used by dsh_dump.py.
# they are tied to db/models.py.
# it's repetition but this is easier for me to understand and manage.
# 

#
# 10-06-08
# --------
# (1)two new types added : OptionalKeyType 
#                         -> models.ForeignKey(KeyWord,blank=True,null=True)
#                      : OptionalSelfsType
#                         -> models.ManyToManyField('self',blank=True,null=True)
#
# (2)OptionalKeyWordsType extended from models.ManyToMany(KeyWord,blank=True)
#                                  to models.ManyToMany(KeyWord,blank=True,null=True)
#


#
# this corresponds to the parent abstract object.
# it contains the fields common to all other object types.
#
DshObjectDef = {
    'dsh_uid': ['StrType'],
    'add_datetime': ['DateType'],
    'save_datetime': ['DateType'],
    'modify_datetime': ['DateType'],
    'description': ['StrType'],
    'comments': ['StrType'],
    'discreet': ['BoolType'],
    'u01': ['StrType'],
    'u02': ['StrType'],
    'u03': ['StrType'],
    'u04': ['StrType'],
    'u05': ['StrType'],
    'u06': ['StrType'],
    'u07': ['StrType'],
    'u08': ['StrType'],
    'u09': ['StrType'],
    'u10': ['StrType'],
    'u11': ['StrType'],
    'u12': ['StrType'],
    'u13': ['IntType'],
    'u14': ['IntType'],
    'u15': ['IntType'],
    'u16': ['IntType'],
    'u17': ['BoolType'],
    'u18': ['BoolType'],
    'u19': ['BoolType'],
    'u20': ['BoolType'],
    'u21': ['BoolType'],
    'u22': ['BoolType'],
    'u23': ['BoolType'],
    'u24': ['BoolType'],
    'u25': ['DateType'],
    'u26': ['DateType'],
    'u27': ['DateType'],
    'u28': ['DateType'],
}


ZObject01Def = {
    'name': ['StrType'],
    'auto_dial_disable': ['BoolType'],
    'scratch_phone_number1': ['StrType'],
    'just_saved_item_dsh_uid': ['StrType'],
    'local_land_line_prefix': ['StrType'],
    'outgoing_channel': ['StrType'],
    'zoiper_number': ['StrType'],
    'asterisk_context': ['StrType'],
    'asterisk_extension': ['StrType'],
    'database_name': ['StrType'],
    'port': ['StrType'],
    'port_lko': ['StrType'],
    'reschedule_wipe_disable': ['StrType'],
    'disable_say_dates': ['BoolType'],
}


ZObject02Def = {
    'name': ['StrType'],
}


ZObject03Def = {
    'name': ['StrType'],
}


ZObject04Def = {
    'name': ['StrType'],
}


ZObject05Def = {
    'name': ['StrType'],
}


ZObject06Def = {
    'name': ['StrType'],
}


ZObject07Def = {
    'name': ['StrType'],
}


ZObject08Def = {
    'name': ['StrType'],
}


KeyWordDef = {
    'key_word': ['StrType'],
    'org_key': ['BoolType'],
    'person_key': ['BoolType'],
}


OrgDef = {
    'name': ['StrType'],
    'alias': ['StrType'],
    'picture': ['FileType'],
    'language': ['StrType'],
    'phone_number': ['StrType'],
    'url': ['StrType'],
    'address': ['StrType'],
    'city_dist': ['StrType'],
    'state_province': ['StrType'],
    'country': ['StrType'],
    'pin': ['StrType'],
    'spoken_name': ['FileType'],
    'org_key_word': ['OptionalKeyType'], 
}


PersonDef = {
    'first_name': ['StrType'],
    'last_name': ['StrType'],
    'phone_number': ['StrType'],
    'phone_owner': ['BoolType'],
    'phone_std': ['BoolType'],
    'phone_landline': ['BoolType'],
    'mugshot': ['FileType'],
    'organization': ['RequiredForeignOrgType'],
    'ptype': ['StrType'],
    'gender': ['StrType'],
    'email': ['StrType'],
    'url': ['StrType'],
    'spoken_name': ['FileType'],
    'timed_broadcast': ['BoolType'],
    'auto_dial_disabled': ['BoolType'],
    'timed1': ['DateType'],
    'timed1_type': ['StrType'],
    'timed2': ['DateType'],
    'timed2_type': ['StrType'],
    'timed3': ['DateType'],
    'timed3_type': ['StrType'],
    'timed4': ['DateType'],
    'timed4_type': ['StrType'],
    'session': ['StrType'],
    'date_birth': ['DateType'],
    'birth_date_approximate': ['BoolType'],
    'age': ['IntType'],
    'birth_date_approximate_change': ['BoolType'],
    'current_dial': ['BoolType'],
    'person_key_words': ['OptionalKeyWordsType'], 
}


ItemDef = {
    'file': ['FileType'],
    'owner': ['RequiredForeignPersonType'],
    'itype': ['StrType'],
    'active': ['BoolType'],
    'starred': ['BoolType'],
    'peer_shared': ['BoolType'],
    'play_once': ['BoolType'],
    'call_duration': ['IntType'],
    'rec_duration': ['IntType'],
    'key_words': ['OptionalKeyWordsType'],
    'followup_to': ['OptionalFollowUpsType'],
    'intended_audience': ['OptionalPersonsType'],
    'i05': ['OptionalOwnerType'],
    'timed1': ['DateType'],
    'timed1_type': ['StrType'],
    'session': ['StrType'],
    'dummy': ['BoolType'],
    'i01': ['OptionalFollowUpsType'],
    'i02': ['OptionalFollowUpsType'],
    'i03': ['OptionalFollowUpsType'],
    'i04': ['OptionalFollowUpsType'],
    'i06': ['OptionalOwnerType'],
    'i07': ['OptionalOwnerType'],
    'i08': ['OptionalOwnerType'],
    'i09': ['OptionalSelfsType'],
    'i10': ['OptionalSelfsType'],
    'i11': ['OptionalSelfsType'],
    'i12': ['OptionalSelfsType'],
    'i13': ['OptionalPersonsType'],
    'i14': ['OptionalPersonsType'],
    'i15': ['OptionalPersonsType'],
    'i16': ['OptionalPersonsType'],
}


EventDef = {
    'etype': ['StrType'],
    'action': ['StrType'],
    'owner': ['OptionalOwnerType'],
    'call_duration': ['IntType'],
    'rec_duration': ['IntType'],
    'dsh_uid_concerned': ['StrType'],
    'debug_tag': ['IntType'],
    'phone_number': ['StrType'],
    'session': ['StrType'],
    'dsh_uid2': ['StrType'], 
}
