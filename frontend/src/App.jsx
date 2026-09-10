import { useState } from "react";
import axios from "axios";
import "./App.css";


function formatRequirementName(name) {
  const specialNames = {
    python: "Python",
    backend_framework: "Backend Framework",
    database_sql: "Database & SQL",
    containerization: "Containerization",
    cloud: "Cloud Platform",
    version_control: "Version Control",
    data_structures: "Data Structures",
    algorithms: "Algorithms",
    rest_api: "REST API",
    skill_backend_development: "Backend Development",
  };

  return (
    specialNames[name] ||
    name
      .replaceAll("_", " ")
      .replace(/\b\w/g, (letter) =>
        letter.toUpperCase()
      )
  );
}


function App() {
  const [file, setFile] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");


  const handleAnalyze = async () => {
    setError("");
    setResult(null);


    // ========================================================
    // VALIDATION
    // ========================================================

    if (!file) {
      setError("Please upload a resume PDF.");
      return;
    }

    if (!jobDescription.trim()) {
      setError("Please enter a job description.");
      return;
    }


    // ========================================================
    // FORM DATA
    // ========================================================

    const formData = new FormData();

    formData.append(
      "file",
      file
    );

    formData.append(
      "job_description",
      jobDescription
    );


    // ========================================================
    // API REQUEST
    // ========================================================

    try {
      setLoading(true);

      const response = await axios.post(
        "http://127.0.0.1:8000/resume/analyze",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      setResult(response.data);

    } catch (err) {

      if (err.response) {
        setError(
          err.response.data.detail ||
          "Something went wrong."
        );
      } else {
        setError(
          "Unable to connect to the backend."
        );
      }

    } finally {
      setLoading(false);
    }
  };


  return (
    <main className="app">

      {/* =====================================================
          HERO
          ===================================================== */}

      <section className="hero">

        <h1>
          AI Resume ATS Analyzer
        </h1>

        <p>
          Upload your resume and compare it with a job description.
        </p>

      </section>


      {/* =====================================================
          ANALYZER FORM
          ===================================================== */}

      <section className="analyzer-card">

        <div className="form-group">

          <label htmlFor="resume">
            Upload Resume (PDF)
          </label>

          <input
            id="resume"
            type="file"
            accept=".pdf,application/pdf"
            onChange={(event) =>
              setFile(event.target.files[0])
            }
          />

          {file && (
            <p className="file-name">
              Selected: {file.name}
            </p>
          )}

        </div>


        <div className="form-group">

          <label htmlFor="job-description">
            Job Description
          </label>

          <textarea
            id="job-description"
            placeholder="Paste the job description here..."
            value={jobDescription}
            onChange={(event) =>
              setJobDescription(event.target.value)
            }
            rows="12"
          />

        </div>


        {/* =================================================
            ERROR
            ================================================= */}

        {error && (
          <div className="error-message">
            {error}
          </div>
        )}


        {/* =================================================
            ANALYZE BUTTON
            ================================================= */}

        <button
          className="analyze-button"
          onClick={handleAnalyze}
          disabled={loading}
        >

          {loading
            ? "Analyzing..."
            : "Analyze Resume"}

        </button>

      </section>


      {/* =====================================================
          RESULTS
          ===================================================== */}

      {result && (
        <section className="results">

          <h2>
            Analysis Result
          </h2>


          {/* =================================================
              ATS SCORE
              ================================================= */}

          <div className="score-card">

            <span>
              ATS Score
            </span>

            <strong>
              {result.ats.ats_score}
              <small>/100</small>
            </strong>

          </div>


          {/* =================================================
              RESUME INFO + RECOMMENDATIONS
              ================================================= */}

          <div className="results-grid">


            {/* RESUME INFORMATION */}

            <div className="result-card">

              <h3>
                Resume Information
              </h3>

              <p>
                <strong>Name:</strong>{" "}
                {result.resume.name || "Not detected"}
              </p>

              <p>
                <strong>Skills:</strong>{" "}
                {result.resume.skills?.length || 0}
              </p>

              <p>
                <strong>Projects:</strong>{" "}
                {result.resume.projects?.length || 0}
              </p>

            </div>


            {/* RECOMMENDATIONS */}

            <div className="result-card">

              <h3>
                Recommendations
              </h3>


              {result.ats.recommendations?.length > 0 ? (

                <ul>

                  {result.ats.recommendations.map(
                    (recommendation, index) => (

                      <li key={index}>
                        {recommendation}
                      </li>

                    )
                  )}

                </ul>

              ) : (

                <p>
                  No recommendations available.
                </p>

              )}

            </div>

          </div>


          {/* =================================================
              JOB REQUIREMENTS
              ================================================= */}

          <div className="result-card requirements">

            <h3>
              Job Requirements
            </h3>


            <div className="requirements-list">

              {Object.entries(
                result.ats.requirements || {}
              ).map(([key, requirement]) => (

                <div
                  className={`requirement ${requirement.status}`}
                  key={key}
                >

                  <div>

                    <strong>
                      {formatRequirementName(
                        requirement.label || key
                      )}
                    </strong>

                    <p>
                      Status: {requirement.status}
                    </p>

                  </div>

                </div>

              ))}

            </div>

          </div>

        </section>
      )}

    </main>
  );
}


export default App;