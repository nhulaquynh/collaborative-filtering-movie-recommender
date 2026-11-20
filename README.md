# Collaborative Filtering for Movie Recommendation

**Đề tài:** Khảo sát phương pháp lọc cộng tác trong hệ thống gợi ý phim: từ độ tương đồng đến đánh giá chất lượng.

## Mục tiêu
Tìm hiểu **User-based KNN** và **Item-based KNN**, cosine similarity trên đánh giá chung, dự đoán điểm đánh giá và cách đánh giá bằng MAE/RMSE.

## Phương pháp
- Đầu vào: ma trận đánh giá người dùng × phim.
- Tính cosine trên phim cùng được đánh giá (User-KNN) hoặc người dùng cùng đánh giá (Item-KNN).
- Dự đoán bằng trung bình trọng số của các láng giềng, giới hạn thang điểm [1,5].
- **Dữ liệu demo là dữ liệu tổng hợp, không phải MovieLens; không xem là kết quả thực nghiệm.**

## Kết quả hiện có
Mã nguồn Python tối giản chạy được bằng thư viện chuẩn, dữ liệu minh họa và các bài kiểm thử. Chưa đánh giá trên dữ liệu thực hay công bố MAE/RMSE thực nghiệm.

## Cấu trúc thư mục
```text
data/          Dữ liệu mẫu và mô tả
src/           Mã nguồn và unittest
docs/          Phương pháp và nguồn tham khảo
results/       Minh chứng chạy demo và unittest
overleaf/      Mã LaTeX và nguồn DOI (cập nhật trong ZIP báo cáo)
figures/       Hình minh họa (trong bộ ZIP Overleaf)
LICENSE        MIT License
CONTRIBUTING.md Hướng dẫn đóng góp
CITATION.cff   Siêu dữ liệu trích dẫn
```

## Hướng dẫn chạy
Yêu cầu Python >=3.9, không cần cài thư viện ngoài.
```bash
python src/recommender.py --input data/ratings.csv --user u1 --item m4 --k 2
python -m unittest discover -s src -p "test_*.py" -v
```

## Báo cáo
Bộ source Overleaf đầy đủ (có hình PDF) được đóng gói riêng để import với **XeLaTeX**. Báo cáo phân tích giấy phép gồm 3 dự án: GNU Bash (GPLv3+), React (MIT), Apache Spark (Apache-2.0).

## Giấy phép
**MIT License** – xem [LICENSE](LICENSE). Giấy phép áp dụng cho mã do dự án tạo; không tự động tái cấp phép dữ liệu hoặc tài nguyên của bên thứ ba.

## Trích dẫn
Xem [CITATION.cff](CITATION.cff). Tên tác giả vẫn cần được xác nhận trước khi công bố chính thức.
