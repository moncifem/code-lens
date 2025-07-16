import Link from "next/link"
import styles from "./analyse.module.css"

export default function AnalysePage() {
  return (
    <div className={styles.container}>
      <main className={styles.main}>
        <div className={styles.hero}>
          <h1 className={styles.title}>
            Analyze Repository
          </h1>

          <p className={styles.description}>
            Enter a Git repository URL to transform it into a searchable knowledge base.
          </p>

          <p className={styles.subtext}>
            Supports all public repositories on GitHub, GitLab, and other Git hosting services.
          </p>
        </div>

        <div className={styles.searchContainer}>
          <div className={styles.searchWrapper}>
            <input
              type="text"
              placeholder="https://github.com/username/repository"
              className={styles.searchInput}
            />
            <button className={styles.searchButton}>
              Analyze
            </button>
          </div>
        </div>

        <div className={styles.features}>
          <div className={styles.feature}>
            <h3>Automated Cloning</h3>
            <p>Repository is automatically cloned and processed with intelligent error handling.</p>
          </div>
          <div className={styles.feature}>
            <h3>Intelligent Chunking</h3>
            <p>Code is parsed by language and chunked for optimal search performance.</p>
          </div>
          <div className={styles.feature}>
            <h3>Vector Search</h3>
            <p>AI-powered search enables natural language queries across your codebase.</p>
          </div>
        </div>

        <div className={styles.backLink}>
          <Link href="/" className={styles.backButton}>
            ← Back to Home
          </Link>
        </div>
      </main>
    </div>
  )
} 