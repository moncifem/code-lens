import Link from "next/link"
import styles from "./Home.module.css"

export default function Home() {
  return (
    <div className={styles.container}>
      <main className={styles.main}>
        <div className={styles.hero}>
          <h1 className={styles.title}>
            CodeLens
          </h1>

          <p className={styles.description}>
            Transform any Git repository into a searchable knowledge base using AI.
          </p>

          <p className={styles.subtext}>
            Perfect for developers, teams, and anyone who needs to understand code quickly.
          </p>
        </div>

        <div className={styles.grid}>
          <Link href="/analyse" className={styles.card}>
            <div className={styles.cardContent}>
              <h2>Analyze Repository</h2>
              <p>Start analyzing a public Git repository with AI-powered insights and intelligent code chunking.</p>
            </div>
            <div className={styles.cardArrow}>→</div>
          </Link>

          <a href="https://github.com/moncifem/code-lens" className={styles.card}>
            <div className={styles.cardContent}>
              <h2>View Source</h2>
              <p>Explore the codebase, contribute to the project, and join the open-source community.</p>
            </div>
            <div className={styles.cardArrow}>→</div>
          </a>
        </div>

        <div className={styles.features}>
          <div className={styles.feature}>
            <h3>Automated Processing</h3>
            <p>Automatically clone and process repositories with intelligent language detection.</p>
          </div>
          <div className={styles.feature}>
            <h3>Smart Chunking</h3>
            <p>Code is intelligently parsed and organized for optimal search performance.</p>
          </div>
          <div className={styles.feature}>
            <h3>Natural Language Search</h3>
            <p>Ask questions about the codebase in plain English and get instant answers.</p>
          </div>
        </div>
      </main>
    </div>
  )
}
