import { Routes, Route, Navigate } from 'react-router-dom';
import { useAuth } from './context/useAuth';
// import { useAuth } from './context/AuthContext';
import LoginPage from './pages/LoginPage';
import TeacherLayout from './pages/TeacherLayout';
import AddLesson from './pages/AddLesson';
import LessonList from './pages/LessonList';  // список занятий (и заданий) в таблице
import TeacherLessons from './pages/TeacherLessons';  
import StudentLayout from './pages/StudentLayout';
import StudentLessons from './pages/StudentLessons';
import StudentCheckLesson from './pages/StudentCheckLesson'; // импортируем компонент

// Защищённый маршрут (можно вынести в отдельный компонент)
const ProtectedRoute = ({ children, allowedRoles }) => {
  const { user } = useAuth();
  if (!user) return <Navigate to="/" replace />;
  if (allowedRoles && !allowedRoles.includes(user.role)) return <Navigate to="/" replace />;
  return children;
};

function App() {
  return (
    <Routes>
      <Route path="/" element={<LoginPage />} />
      <Route
        path="/teacher"
        element={
          <ProtectedRoute allowedRoles={['teacher']}>
            <TeacherLayout />
          </ProtectedRoute>
        }
      >
        <Route index element={<Navigate to="lessons" replace />} />

        {/* 1-й вариант - список занятий (и заданий) в таблице */}
        {/* <Route path="lessons" element={<LessonList />} />   */}

        {/* 2-й вариант - список занятий в виде карточек */}  
        <Route path="lessons" element={<TeacherLessons  />} /> 
        <Route path="add-lesson" element={<AddLesson />} />
      </Route>


      <Route
        path="/student"
        element={
          <ProtectedRoute allowedRoles={['student']}>
            {/* <div>Страница студента (в разработке)</div> */}
            <StudentLayout />        
          </ProtectedRoute>
        }
      >
        <Route index element={<Navigate to="lessons" replace />} />
        <Route path="lessons" element={<StudentLessons />} />
        <Route path="check/:lessonId" element={<StudentCheckLesson />} />
        {/* другие страницы студента можно добавить позже */}
      </Route>
    </Routes>
  );
}

export default App;
