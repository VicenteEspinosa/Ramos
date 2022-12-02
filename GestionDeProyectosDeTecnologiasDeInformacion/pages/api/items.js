// Next.js API route support: https://nextjs.org/docs/api-routes/introduction

export default function handler(req, res) {
  res.status(200).json([
    {
      id: 0,
      title: "Lollapalooza 2023",
      date: "17 / 03   -   19 / 03",
      price: 130,
      image: "http://localhost:3000/img/lollapalooza.jpeg",
      description:
        "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Officia maiores praesentium vitae sequi consectetur itaque ea inventore architecto nemo. Enim id perspiciatis minus modi qui at commodi quos quisquam similique!",
    },
    {
      id: 1,
      title: "Oktoberfest 2022",
      date: "28 / 10   -   01 / 11",
      price: 12,
      image: "http://localhost:3000/img/oktoberfest.jpeg",
      description:
        "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Officia maiores praesentium vitae sequi consectetur itaque ea inventore architecto nemo. Enim id perspiciatis minus modi qui at commodi quos quisquam similique!",
    },
    {
      id: 2,
      title: "Creamfields 2022",
      date: "05 / 11  -   06 / 11",
      price: 64,
      image: "http://localhost:3000/img/creamfields.jpeg",
      description:
        "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Officia maiores praesentium vitae sequi consectetur itaque ea inventore architecto nemo. Enim id perspiciatis minus modi qui at commodi quos quisquam similique!",
    },
  ]);
}
