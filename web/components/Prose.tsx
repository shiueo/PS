export const Prose: React.FC<{
  children: React.ReactNode
}> = ({ children }) => {
  return (
    <div className="prose max-w-none prose-a:text-pink-600 dark:prose-invert">
      {children}
    </div>
  )
}
