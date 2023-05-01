const configuration = {
  site: {
    name: 'shiüo - PS',
    description:
      'MakerKit is the SaaS starter built with Next.js, Firebase and' +
      ' Tailwind that lets you launch your next idea in minutes.',
    themeColor: '#ff0a54',
    siteUrl: 'https://makerkit.dev',
    siteName: 'shiüo - PS',
    twitterHandle: 'shiueo_csh',
    githubHandle: 'shiueo',
    language: 'en',
  },
  blog: {
    maxReadMorePosts: 6,
  },
  production: process.env.NODE_ENV === 'production',
};

export default configuration;
