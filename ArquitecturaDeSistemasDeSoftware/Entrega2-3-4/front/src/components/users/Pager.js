import { Pagination } from "react-bulma-components";

const ELEMENTS_PER_PAGE = 5;

const Pager = ({ id = "pagination", elementsCount, currentPage, onChangeFunction, perPage = ELEMENTS_PER_PAGE }) => {
    const pages = Math.ceil(elementsCount / perPage);

    return (
        <Pagination
            id={id}
            current={currentPage}
            showFirstLast
            total={pages}
            onChange={onChangeFunction}
            align={"center"}
        />
    );
};

export default Pager;