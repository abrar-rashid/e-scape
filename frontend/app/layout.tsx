import type { Metadata } from "next";
import { inter } from './fonts'
import "./globals.css";
// import localFont from "next/font/local";

// const pirate = localFont({
//   src: [
//     {
//       path: '../../public/fonts/pirate_font.ttf',
//       weight: '400'
//     }
//   ],
//   variable: '--font-pirate'
// })

export const metadata: Metadata = {
  title: "Create Next App",
  description: "Generated by create next app",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
    {/* <html lang="en" className={`${pirate.variable} font-sans`}> */}
      <body className={`${inter.className} text-center`}>{children}</body>
    </html>
  );
}
