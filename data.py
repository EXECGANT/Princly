# Main Category
#? Only Get Method
mainCategory = [
  {'category_id': 1, 'category_name': 'University'},
  {'category_id': 2, 'category_name': 'Competitive Exam'},
  {'category_id': 3, 'category_name': 'School'},
  {'category_id': 4, 'category_name': 'Computer Course'},
]

# University #? CRUD Operation
university = [
  {
    'university_id': 1,
    'university_name': 'Anna University',
    'university_image':
        'https://onlinecde.annauniv.edu/pluginfile.php/1/local_mb2builder/images/Anna%20University-Front.jpg',
  },
  {
    'university_id': 2,
    'university_name': 'Annamalai University',
    'university_image':
        'https://psychoprodigy.in/sites/default/files/inline-images/1_0.jpg',
  },
]

university_courses = [
  {'university_id': 1, 'course_name': 'Engineering', 'course_id': 1},
  {'university_id': 1, 'course_name': 'Art', 'course_id': 2},
  {'university_id': 1, 'course_name': 'Science', 'course_id': 3},
  {'university_id': 2, 'course_name': 'Engineering', 'course_id': 4},
  {'university_id': 2, 'course_name': 'Medical', 'course_id': 5},
  {'university_id': 2, 'course_name': 'Science', 'course_id': 6},
]

university_course_degree = [
  {'course_id': 1, 'degree_name': 'B.E', 'degree_id': 1},
  {'course_id': 1, 'degree_name': 'M.E', 'degree_id': 2},
  {'course_id': 2, 'degree_name': 'B.A', 'degree_id': 3},
  {'course_id': 2, 'degree_name': 'M.A', 'degree_id': 4},
  {'course_id': 3, 'degree_name': 'B.Sc', 'degree_id': 5},
  {'course_id': 3, 'degree_name': 'M.Sc', 'degree_id': 6},
  {'course_id': 4, 'degree_name': 'B.E', 'degree_id': 7},
  {'course_id': 4, 'degree_name': 'M.E', 'degree_id': 8},
  {'course_id': 5, 'degree_name': 'MBBS', 'degree_id': 9},
  {'course_id': 5, 'degree_name': 'MD', 'degree_id': 10},
  {'course_id': 6, 'degree_name': 'B.Sc', 'degree_id': 11},
  {'course_id': 6, 'degree_name': 'M.Sc', 'degree_id': 12},
]

university_course_degree_year = [
  {'year_id': 1, 'year_name': '1999-2007', 'degree_id': 1},
  {'year_id': 1, 'year_name': '2008-2013', 'degree_id': 2},
  {'year_id': 2, 'year_name': '2013-2017', 'degree_id': 3},
]

university_course_degree_year_semester = [
  {'year_id': 1, 'semester_id': 1, 'semester_name':'Semester 1'},
  {'year_id': 1, 'semester_id': 2, 'semester_name':'Semester 2'},
  {'year_id': 1, 'semester_id': 3, 'semester_name':'Semester 3'},
  {'year_id': 1, 'semester_id': 4, 'semester_name':'Semester 4'},
  {'year_id': 1, 'semester_id': 5, 'semester_name':'Semester 5'},
  {'year_id': 1, 'semester_id': 6, 'semester_name':'Semester 6'},
  {'year_id': 1, 'semester_id': 7, 'semester_name':'Semester 7'},
  {'year_id': 1, 'semester_id': 8, 'semester_name':'Semester 8'},
  {'year_id': 2, 'semester_id': 1, 'semester_name':'Semester 9'},
  {'year_id': 2, 'semester_id': 2, 'semester_name':'Semester 10'},
  {'year_id': 2, 'semester_id': 3, 'semester_name':'Semester 11'},
  {'year_id': 2, 'semester_id': 4, 'semester_name':'Semester 12'},
  {'year_id': 2, 'semester_id': 5, 'semester_name':'Semester 13'},
  {'year_id': 2, 'semester_id': 6, 'semester_name':'Semester 14'},
  {'year_id': 2, 'semester_id': 7, 'semester_name':'Semester 15'},
  {'year_id': 2, 'semester_id': 8, 'semester_name':'Semester 16'},
]

university_course_degree_year_semester_subject = [
  {'semester': 1, 'subject_name': 'Maths', 'subject_id': 1},
  {'semester': 1, 'subject_name': 'Physics', 'subject_id': 2},
  {'semester': 1, 'subject_name': 'Chemistry', 'subject_id': 3},
  {'semester': 2, 'subject_name': 'Maths', 'subject_id': 4},
  {'semester': 2, 'subject_name': 'Physics', 'subject_id': 5},
  {'semester': 2, 'subject_name': 'Chemistry', 'subject_id': 6},
  {'semester': 3, 'subject_name': 'Maths', 'subject_id': 7},
  {'semester': 3, 'subject_name': 'Physics', 'subject_id': 8},
  {'semester': 3, 'subject_name': 'Chemistry', 'subject_id': 9},
  {'semester': 4, 'subject_name': 'Maths', 'subject_id': 10},
  {'semester': 4, 'subject_name': 'Physics', 'subject_id': 11},
  {'semester': 4, 'subject_name': 'Chemistry', 'subject_id': 12},
  {'semester': 5, 'subject_name': 'Maths', 'subject_id': 13},
  {'semester': 5, 'subject_name': 'Physics', 'subject_id': 14},
  {'semester': 5, 'subject_name': 'Chemistry', 'subject_id': 15},
  {'semester': 6, 'subject_name': 'Maths', 'subject_id': 16},
  {'semester': 6, 'subject_name': 'Physics', 'subject_id': 17},
  {'semester': 6, 'subject_name': 'Chemistry', 'subject_id': 18},
  {'semester': 7, 'subject_name': 'Maths', 'subject_id': 19},
  {'semester': 7, 'subject_name': 'Physics', 'subject_id': 20},
  {'semester': 7, 'subject_name': 'Chemistry', 'subject_id': 21},
  {'semester': 8, 'subject_name': 'Maths', 'subject_id': 22},
  {'semester': 8, 'subject_name': 'Physics', 'subject_id': 23},
]

university_course_degree_year_semester_subject_video = [
  {
    'subject_id': 1,
    'video_url': 'https://youtu.be/jqdb-4iURJk?si=EXsINBO_XSR00NT1',
    'video_id': 1,
  },
  {
    'subject_id': 1,
    'video_url': 'https://youtu.be/LBOgBuucQOI?si=srer2kEsAZzY-E3J',
    'video_id': 2,
  },
  {
    'subject_id': 2,
    'video_url': 'https://youtu.be/LBOgBuucQOI?si=srer2kEsAZzY-E3J',
    'video_id': 3,
  },
  {
    'subject_id': 3,
    'video_url': 'https://youtu.be/1tFzMFrduks?si=JceO-i33_VN9YEze',
    'video_id': 4,
  },
  {
    'subject_id': 3,
    'video_url': 'https://youtu.be/qpPZeAj6lGU?si=GyKD3tZUOklAfsGz',
    'video_id': 5,
  },
  {
    'subject_id': 3,
    'video_url': 'https://youtu.be/KSNJGvl0P_0?si=wl9tcEupnGpAkqIF',
    'video_id': 6,
  },
  {
    'subject_id': 4,
    'video_url': 'https://youtu.be/oM0XaXs1fCw?si=CQTsO51YtuF-73Ab',
    'video_id': 7,
  },
]


# Competitive Exam #? CRUD Operation
competitive_exams = [
  {'exam_name': 'JEE', 'exam_id': 1, 'exam_image' : 'url'},
  {'exam_name': 'NEET', 'exam_id': 2, 'exam_image' : 'url'},
  {'exam_name': 'UPSC', 'exam_id': 3, 'exam_image' : 'url'},
]

competitive_exam_subject = [
  {'exam_id': 1, 'subject_name': 'Physics', 'subject_id': 1},
  {'exam_id': 1, 'subject_name': 'Chemistry', 'subject_id': 2},
  {'exam_id': 1, 'subject_name': 'Maths', 'subject_id': 3},
  {'exam_id': 2, 'subject_name': 'Physics', 'subject_id': 4},
  {'exam_id': 2, 'subject_name': 'Chemistry', 'subject_id': 5},
  {'exam_id': 2, 'subject_name': 'Biology', 'subject_id': 6},
  {'exam_id': 3, 'subject_name': 'History', 'subject_id': 7},
  {'exam_id': 3, 'subject_name': 'Geography', 'subject_id': 8},
  {'exam_id': 3, 'subject_name': 'Polity', 'subject_id': 9},
]

competitive_exam_subject_video = [
  {
    'subject_id': 1,
    'video_url': 'https://youtu.be/jqdb-4iURJk?si=EXsINBO_XSR00NT1',
    'video_id': 1,
  },
  {
    'subject_id': 1,
    'video_url': 'https://youtu.be/LBOgBuucQOI?si=srer2kEsAZzY-E3J',
    'video_id': 2,
  },
  {
    'subject_id': 2,
    'video_url': 'https://youtu.be/LBOgBuucQOI?si=srer2kEsAZzY-E3J',
    'video_id': 3,
  },
  {
    'subject_id': 3,
    'video_url': 'https://youtu.be/1tFzMFrduks?si=JceO-i33_VN9YEze',
    'video_id': 4,
  },
  {
    'subject_id': 3,
    'video_url': 'https://youtu.be/qpPZeAj6lGU?si=GyKD3tZUOklAfsGz',
    'video_id': 5,
  },
  {
    'subject_id': 3,
    'video_url': 'https://youtu.be/KSNJGvl0P_0?si=wl9tcEupnGpAkqIF',
    'video_id': 6,
  },
  {
    'subject_id': 3,
    'video_url': 'https://youtu.be/oM0XaXs1fCw?si=CQTsO51YtuF-73Ab',
    'video_id': 7,
  },
]

# School #? CRUD Operation
school_data = [
  {'school_name': 'CBSC', 'school_id': 1, 'school_image' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Staples_High_School%2C_Westport%2C_CT.jpg/1200px-Staples_High_School%2C_Westport%2C_CT.jpg'},
  {'school_name': 'METRIC', 'school_id': 2, 'school_image' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Staples_High_School%2C_Westport%2C_CT.jpg/1200px-Staples_High_School%2C_Westport%2C_CT.jpg'},
  {'school_name': 'GOVERN', 'school_id': 3, 'school_image' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Staples_High_School%2C_Westport%2C_CT.jpg/1200px-Staples_High_School%2C_Westport%2C_CT.jpg'},
]

school_classes = [
  {'school_id': 1, 'class_name': '1st', 'class_id': 1},
  {'school_id': 1, 'class_name': '2nd', 'class_id': 2},
  {'school_id': 1, 'class_name': '3rd', 'class_id': 3},
  {'school_id': 2, 'class_name': '1st', 'class_id': 4},
  {'school_id': 2, 'class_name': '2nd', 'class_id': 5},
  {'school_id': 2, 'class_name': '3rd', 'class_id': 6},
  {'school_id': 3, 'class_name': '1st', 'class_id': 7},
  {'school_id': 3, 'class_name': '2nd', 'class_id': 8},
  {'school_id': 3, 'class_name': '3rd', 'class_id': 9},
];

school_class_subjects = [
  {'class_id': 1, 'subject_name': 'Maths', 'subject_id': 1},
  {'class_id': 1, 'subject_name': 'Science', 'subject_id': 2},
  {'class_id': 1, 'subject_name': 'English', 'subject_id': 3},
  {'class_id': 2, 'subject_name': 'Maths', 'subject_id': 4},
  {'class_id': 2, 'subject_name': 'Science', 'subject_id': 5},
  {'class_id': 2, 'subject_name': 'English', 'subject_id': 6},
  {'class_id': 3, 'subject_name': 'Maths', 'subject_id': 7},
  {'class_id': 3, 'subject_name': 'Science', 'subject_id': 8},
  {'class_id': 3, 'subject_name': 'English', 'subject_id': 9},
  {'class_id': 4, 'subject_name': 'Maths', 'subject_id': 10},
  {'class_id': 4, 'subject_name': 'Science', 'subject_id': 11},
  {'class_id': 4, 'subject_name': 'English', 'subject_id': 12},
  {'class_id': 5, 'subject_name': 'Maths', 'subject_id': 13},
  {'class_id': 5, 'subject_name': 'Science', 'subject_id': 14},
  {'class_id': 5, 'subject_name': 'English', 'subject_id': 15},
  {'class_id': 6, 'subject_name': 'Maths', 'subject_id': 16},
  {'class_id': 6, 'subject_name': 'Science', 'subject_id': 17},
  {'class_id': 6, 'subject_name': 'English', 'subject_id': 18},
  {'class_id': 7, 'subject_name': 'Maths', 'subject_id': 19},
  {'class_id': 7, 'subject_name': 'Science', 'subject_id': 20},
  {'class_id': 7, 'subject_name': 'English', 'subject_id': 21},
  {'class_id': 8, 'subject_name': 'Maths', 'subject_id': 22},
];

school_class_subjects_video = [
  {
    'subject_id': 1,
    'video_url': 'https://youtu.be/jqdb-4iURJk?si=EXsINBO_XSR00NT1',
    'video_id': 1,
  },
  {
    'subject_id': 1,
    'video_url': 'https://youtu.be/LBOgBuucQOI?si=srer2kEsAZzY-E3J',
    'video_id': 2,
  },
  {
    'subject_id': 2,
    'video_url': 'https://youtu.be/LBOgBuucQOI?si=srer2kEsAZzY-E3J',
    'video_id': 3,
  },
  {
    'subject_id': 3,
    'video_url': 'https://youtu.be/1tFzMFrduks?si=JceO-i33_VN9YEze',
    'video_id': 4,
  },
  {
    'subject_id': 3,
    'video_url': 'https://youtu.be/qpPZeAj6lGU?si=GyKD3tZUOklAfsGz',
    'video_id': 5,
  },
  {
    'subject_id': 3,
    'video_url': 'https://youtu.be/KSNJGvl0P_0?si=wl9tcEupnGpAkqIF',
    'video_id': 6,
  },
  {
    'subject_id': 4,
    'video_url': 'https://youtu.be/oM0XaXs1fCw?si=CQTsO51YtuF-73Ab',
    'video_id': 7,
  },
];


# Computer Course #? CRUD Operation
computer_courses = [
  {'course_name': 'Web Development', 'course_id': 1, 'course_image' : 'url'},
  {'course_name': 'Mobile App Development', 'course_id': 2, 'course_image' : 'url'},
]

computer_course_subject = [
  {'course_id': 1, 'subject_name': 'HTML', 'subject_id': 1},
  {'course_id': 1, 'subject_name': 'CSS', 'subject_id': 2},
  {'course_id': 1, 'subject_name': 'JavaScript', 'subject_id': 3},
  {'course_id': 1, 'subject_name': 'React', 'subject_id': 4},
  {'course_id': 1, 'subject_name': 'Node.js', 'subject_id': 5},
  {'course_id': 1, 'subject_name': 'MongoDB', 'subject_id': 6},
  {'course_id': 2, 'subject_name': 'Dart', 'subject_id': 7},
  {'course_id': 2, 'subject_name': 'Flutter', 'subject_id': 8},
  {'course_id': 2, 'subject_name': 'Firebase', 'subject_id': 9},
  {'course_id': 2, 'subject_name': 'Android Studio', 'subject_id': 10},
  {'course_id': 2, 'subject_name': 'Xcode', 'subject_id': 11},
  {'course_id': 2, 'subject_name': 'Swift', 'subject_id': 12},
]

computer_course_subject_video = [
  {
    'subject_id': 1,
    'video_url': 'https://youtu.be/jqdb-4iURJk?si=EXsINBO_XSR00NT1',
    'video_id': 1,
  },
  {
    'subject_id': 1,
    'video_url': 'https://youtu.be/LBOgBuucQOI?si=srer2kEsAZzY-E3J',
    'video_id': 2,
  },
  {
    'subject_id': 2,
    'video_url': 'https://youtu.be/LBOgBuucQOI?si=srer2kEsAZzY-E3J',
    'video_id': 3,
  },
  {
    'subject_id': 3,
    'video_url': 'https://youtu.be/1tFzMFrduks?si=JceO-i33_VN9YEze',
    'video_id': 4,
  },
  {
    'subject_id': 3,
    'video_url': 'https://youtu.be/qpPZeAj6lGU?si=GyKD3tZUOklAfsGz',
    'video_id': 5,
  },
  {
    'subject_id': 4,
    'video_url': 'https://youtu.be/KSNJGvl0P_0?si=wl9tcEupnGpAkqIF',
    'video_id': 6,
  },
  {
    'subject_id': 5,
    'video_url': 'https://youtu.be/oM0XaXs1fCw?si=CQTsO51YtuF-73Ab',
    'video_id': 7,
  },
]




