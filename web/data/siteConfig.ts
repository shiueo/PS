import type { SiteConfig } from "@/lib/types";
const siteConfig: SiteConfig = {
  avatar: "/avatar.png",
  siteUrl: "https://shiueo-ps.vercel.app",
  siteName: "shiüo PS",
  siteDescription:
    "shiüo's PS Blog",
  siteThumbnail: "/og-image.png",
  nav: [
    { label: "Posts", href: "/posts" },
    { label: "About", href: "/about" },
  ],
  social: {
    github: "https://github.com/shiueo",
    twitter: "https://twitter.com/shiueo_csh",
    youtube: "https://youtube.com/@shiueo",
  },
};
export default siteConfig;
