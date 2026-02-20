import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import AceEditor from 'react-ace';
import api from '../api';
import checkingApi from '../api/checkingApi';

// Импорт необходимых режимов и тем для AceEditor
import 'ace-builds/src-noconflict/mode-python';
import 'ace-builds/src-noconflict/mode-csharp';  // Импортируем режим для C#
import 'ace-builds/src-noconflict/theme-monokai';  // Импортируем тему - темная 1
import 'ace-builds/src-noconflict/theme-twilight'; // темная 2
import 'ace-builds/src-noconflict/theme-solarized_dark';  // темная 3

const StudentCheckLesson = () => {
  const { lessonId } = useParams();
  const [lesson, setLesson] = useState(null);
  const [code, setCode] = useState(`// Введите ваше решение на C# ниже
// Пример программы Hello World:
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Hello, World!");
    }
}`);
  const [output, setOutput] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const fetchLesson = async () => {
      try {
        const res = await api.get(`/lessons/${lessonId}`);
        setLesson(res.data);
      } catch (error) {
        console.error('Ошибка загрузки задания:', error);
      }
    };
    fetchLesson();
  }, [lessonId]);

  const handleCompile = async () => {
    setLoading(true);
    try {
      const res = await checkingApi.post('/compile', { code, lessonId });
      setOutput(res.data.output);
    } catch (err) {
      setOutput('Ошибка компиляции!');
    } finally {
      setLoading(false);
    }
  };

  const handleTest = async () => {
    setLoading(true);
    try {
      const res = await checkingApi.post('/test', { code, lessonId });
      setOutput(res.data.result);
    } catch (err) {
      setOutput('Ошибка тестирования!');
    } finally {
      setLoading(false);
    }
  };

  if (!lesson) return <div className="loading">Загрузка...</div>;

  return (
    <div className="check-container">
      <h2>Проверка задания {lesson.assignment_number}</h2>
      <strong>Описание:</strong> {lesson.assignment_description}

      {/* Пояснение для студента */}
      {/* <div style={{ margin: '10px 0 5px 0' }}>
        <span style={{ fontStyle: 'italic', color: '#253daaff' }}>Введите код вашего решения на C#.</span>
      </div> */}
      <span style={{ fontStyle: 'italic', color: '#203180ff', display: 'block', marginTop: '10px', marginBottom: '5px' }}>
        Введите код вашего решения на C#.
      </span>
      {/* Обёртка для закруглённого редактора */}
      <div className="code-editor-wrapper">
        <AceEditor
            mode="csharp"  // "python"
            theme="monokai"  // "monokai", "twilight", "solarized_dark"
            name="code-editor"
            onChange={setCode}
            value={code}
            fontSize={14}
            width="100%"
            height="400px"
            editorProps={{ $blockScrolling: true }}
            setOptions={{
            enableBasicAutocompletion: true,
            enableLiveAutocompletion: true,
            showLineNumbers: true,
            tabSize: 2,
            }}
        />
      </div>
      <div className="lesson-actions">
        <button
          className="button-small check-btn"
          onClick={handleCompile}
          disabled={loading}
        >
          Компилировать
        </button>
        <button
          className="button-small upload-btn"
          onClick={handleTest}
          disabled={loading}
        >
          Тестировать
        </button>
      </div>

      {/* Заголовок для результатов */}
      <span style={{ fontStyle: 'italic', color: '#203180ff', display: 'block', marginTop: '10px', marginBottom: '5px' }}>
        Результаты компиляции / тестирования
      </span>
      <div className="output-wrapper">
        <pre className="output">
          {output || (loading ? 'Выполняется...' : 'Окно вывода результатов')}
        </pre>
      </div>
    </div>
  );
};

export default StudentCheckLesson;